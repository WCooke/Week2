#include <stdio.h>
int main()
{
  char Password[10];
  printf ("Please enter the Password: ");
  scanf( "%s" ,Password );
  if (strcmp(Password, "Hello") == 0 ) 
  {
    printf  ("Welcome to the secret manifesto (Don't show to others) )  ");
  }
  else 
  {
    printf ("Sorry that Password is incorect, stay away. ");
  }
return 0;
}
