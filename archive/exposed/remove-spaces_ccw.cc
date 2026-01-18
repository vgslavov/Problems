int i = 0 , j = 0; 

while (str[j]) { 
    if (str[j] != ' ') 
        str[i++] = str[j]; 
    ++j; 
} 

str[j] = '\0';
