`typedef struct CEO {`  
    `const char* name;`  
    `const char* location;`  
    `const char* growthGoals;`  
    `int growthPercent;`  
`} CEO;`  
   
`typedef struct Connection {`  
    `const char* name;`  
    `const char* location;`  
    `int hasExperienceWithCAndCpp;`  
    `int numberOfLinesInPreviousCodeBase;`  
    `int numberOfTop50BanksUsingCodeBase;`  
    `const char* email;`  
    `const char* phone;`  
`} Connection;`  
   
`int openToConversation(const CEO* ceo, const Connection* consultant);`  
`void sendEmailOrText(const CEO* ceo, const char* email,`  
                     `const char* phone);`  
   
`int main() {`  
    `CEO ceo;`  
    `ceo.name = "Mike Juran";`  
    `ceo.location = "Colorado Springs, CO";`  
    `ceo.growthGoals = "aggressive";`  
    `ceo.growthPercent = 40;`   
   
    `Connection connection;`  
    `connection.name = "Matthias Miller";`  
    `connection.location = "Florence, CO";`  
    `connection.hasExperienceWithCAndCpp = 1;`  
    `connection.numberOfLinesInPreviousCodeBase = 1500000;`  
    `connection.numberOfTop50BanksUsingCodeBase = 45;`   
    `connection.email = "matthias.miller@codehaus.com";`  
    `connection.phone = "+17194581650";`  
   
    `if (openToConversation(&ceo, &connection))`  
        `sendEmailOrText(&ceo, connection.email, connection.phone);`

    `return 0;`  
`}`
