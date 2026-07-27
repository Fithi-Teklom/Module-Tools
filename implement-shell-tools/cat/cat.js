const fs = require("fs");

const args = process.argv.slice(2);

let mode = "normal";
let files = [];

if (args[0] === "-n") {
  mode = "number";
  files = args.slice(1);
} else if (args[0] === "-b") {
  mode = "numberNonEmpty";
  files = args.slice(1);
} else {
  files = args;
}

let lineNum = 1;

for (const file of files) {
  const content = fs.readFileSync(file, "utf8");

  const lines = content.replace(/\n$/, "").split("\n");

  if (mode === "normal") {
    console.log(content);
    continue;
  }

  for (const line of lines) {
    if (mode === "number") {
      console.log(`${String(lineNum).padStart(6)}  ${line}`);
      lineNum++;
    } else if (mode === "numberNonEmpty") {
      if (line === "") {
        console.log("");
      } else {
        console.log(`${String(lineNum).padStart(6)}  ${line}`);
        lineNum++;
      }
    }
  }
}
