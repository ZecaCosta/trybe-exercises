const greetingMessage = (user) => {
    return `Hello, ${user}! Que bom ter você de volta`;
};

const loginErrorMessage = (user) => {
    return `Pessoa usuária '${user}' não encontrada, tente novamente!`
};

const user = {
    userName: "Joana",
    password: 123456,
};

const verifyCredentials = (user) => {
    if (user.password === 123456 && user.userName === "Joana") {
        return greetingMessage(user.userName);
    } else {
        return loginErrorMessage(user.userName);
    }
};

module.exports = { greetingMessage, loginErrorMessage, verifyCredentials }