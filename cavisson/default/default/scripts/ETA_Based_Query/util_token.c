#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//#include <openssl/sha.h>
#include "ns_string.h"

char *base64URLEncode(char *str) {
  // replace +, /  into _ and = into '' (empty string)
  int in = 0, out = 0;
  int len = strlen(str);

  for (; in < len; in++) {
    if (str[in] == '/') {
      str[out++] = '_';
    } else if (str[in] == '+') {
      str[out++] = '-';	   
    } else if (str[in] != '=') {
      str[out++] = str[in];
    }
  }

  str[out] = 0;
  return str;
}

int get_hash256(void *data, unsigned long length, unsigned char* payloadHash)
{
      unsigned char myHash[SHA256_DIGEST_LENGTH];
      int i;
      SHA256_CTX context;

      if(!SHA256_Init(&context))
          return 1;

      if(!SHA256_Update(&context, (unsigned char*)data, length))
          return 1;

      if(!SHA256_Final(myHash, &context))
          return 1;

      //for(i=0; i<SHA256_DIGEST_LENGTH; i++)
      //  sprintf((char*)(payloadHash + (i*2)), "%02x", myHash[i]);
      memcpy(payloadHash, myHash, SHA256_DIGEST_LENGTH);

      return 0;
}

int fill_code_verifier_param(char *param_name) {
  // create code verified. 
  char random_str[32 + 1];
  char random_str_encoded[128];
  strcpy(random_str, ns_get_random_str(32, 32, "a-zA-Z0-9"));
  printf("random_str - %s\n", random_str);

  strcpy(random_str_encoded, ns_encode_base64(random_str, 32, NULL));
  printf("random_str_encoded - %s\n", random_str_encoded);

  base64URLEncode(random_str_encoded);
  printf("random_str_encoded with uri base64 - %s\n", random_str_encoded);

  // save parameter value.
  return ns_save_string(random_str_encoded, param_name);
}

int fill_code_challenge_param(char *param_name, char *code_verifier) {
  unsigned char sha256_hash[64 +1] = {0};

  get_hash256(code_verifier, strlen(code_verifier), sha256_hash);

  char encoded_hash[256];
  //strcpy(encoded_hash, ns_encode_base64(sha256_hash, SHA256_DIGEST_LENGTH, NULL));
  ns_encode_base64_binary(sha256_hash, SHA256_DIGEST_LENGTH, encoded_hash, 256);
  printf("Base64 encoded hash - %s\n", encoded_hash);

  base64URLEncode(encoded_hash);

  printf("code challenge - %s\n", encoded_hash);

  return ns_save_string(encoded_hash, param_name);
}
