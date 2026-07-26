const fs = require("fs");

const args = process.argv.slice(2);

let mode = "normal";

if (args[0] === "-b") {
  mode = "numberNonEmpty";
}

const files = args.slice(1);

let lineNum = 1;

for (const file of files) {

  const content = fs.readFileSync(file, "utf8");

  const lines = content.trimEnd().split("\n");

  for (const line of lines) {

    if (mode === "numberNonEmpty") {

      if (line !== "") {
        console.log(lineNum + " " + line);
        lineNum++;
      } else {
        console.log(line);
      }

    }

  }
}
