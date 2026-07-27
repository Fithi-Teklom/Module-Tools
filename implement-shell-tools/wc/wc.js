const fs = require("fs");
const path = require("path");

const args = process.argv.slice(2);

let countLines = false;
let countWords = false;
let countBytes = false;

let files = [];

for (const arg of args) {
  if (arg === "-l") {
    countLines = true;
  } else if (arg === "-w") {
    countWords = true;
  } else if (arg === "-c") {
    countBytes = true;
  } else {
    files.push(arg);
  }
}

function expandWildcard(filePath) {
  if (!filePath.includes("*")) {
    return [filePath];
  }

  const dir = path.dirname(filePath);
  const files = fs.readdirSync(dir);

  return files.map(file => path.join(dir, file));
}

function getStats(filename) {

  const content = fs.readFileSync(filename, "utf8");

  const lines = content.split("\n").length - 1;

  const words = content
    .trim()
    .split(/\s+/)
    .filter(word => word.length > 0)
    .length;

  const bytes = fs.statSync(filename).size;

  return {
    lines,
    words,
    bytes
  };
}

function printResult(stats, filename, showFilename = true) {

  let output = [];

  if (!countLines && !countWords && !countBytes) {
    output.push(stats.lines);
    output.push(stats.words);
    output.push(stats.bytes);
  } else {
    if (countLines) {
      output.push(stats.lines);
    }

    if (countWords) {
      output.push(stats.words);
    }

    if (countBytes) {
      output.push(stats.bytes);
    }
  }

  if (showFilename) {
    output.push(filename);
  }

  console.log(output.join(" "));
}

let allFiles = [];

for (const file of files) {
  allFiles.push(...expandWildcard(file));
}

let total = {
  lines: 0,
  words: 0,
  bytes: 0
};

for (const file of allFiles) {

  const stats = getStats(file);

  total.lines += stats.lines;
  total.words += stats.words;
  total.bytes += stats.bytes;

  printResult(stats, file);
}
if (allFiles.length > 1) {
  printResult(total, "total");
}