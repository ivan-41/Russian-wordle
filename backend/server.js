import word_pool from "./Secret_words";

// функция выбора случайного слова
function SetRandWord() {
    let rand = Math.floor(Math.random() * word_pool.length);
    return word_pool[rand];
};

var secret_word_tod = SetRandWord();
console.log(secret_word_tod);

//для повторныого выбора секретного слова:
//SetRandWord();
//var secret_word_tod = SetRandWord();