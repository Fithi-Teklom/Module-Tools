const fs = require ("fs");
const args = process.argv.slice(2);
const content = fs.readFileSync(args[0], "utf-8")
console.log(content);