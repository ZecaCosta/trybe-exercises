const {
    greetingMessage,
    loginErrorMessage,
    verifyCredentials,
} = require("./loginValidation");

describe("teste da função verifyCredentials()", () => {
    it("verifyCredentials() calls the correct function dependending on user and password input", () => {
        const user = {
            userName: "Joana",
            password: 123456,
        };
        expect(verifyCredentials(user)).toBe(
            "Hello, Joana! Que bom ter você de volta"
        );
    });

    it("greetingMessage() returns a message in the format: `Hello, ${user}! Que bom ter você de volta`", () => {
        expect(greetingMessage("Lucas")).toBe(
          "Hello, Lucas! Que bom ter você de volta"
        );
      });
    
      it("loginErrorMessage() returns a message in the format: `Pessoa usuária '${user}' não encontrada, tente novamente!`", () => {
        expect(loginErrorMessage("Bob")).toBe(
          "Pessoa usuária 'Bob' não encontrada, tente novamente!"
        );
      });
});