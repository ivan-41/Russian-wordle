// загружаем слова из файла в массив
let fs = require('fs');
const word_pool = fs.readFileSync('Dictionary/Secret_words.txt').toString().split("\n");