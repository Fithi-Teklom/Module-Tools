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

let results = [];

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

  results.push({
    stats,
    filename: file
  });
}
if (allFiles.length > 1) {
  results.push({
    stats: total,
    filename: "total"
  });
}


let lineWidth = 0;
let wordWidth = 0;
let byteWidth = 0;

for (const result of results) {
  lineWidth = Math.max(
    lineWidth,
    String(result.stats.lines).length
  );

  wordWidth = Math.max(
    wordWidth,
    String(result.stats.words).length
  );

  byteWidth = Math.max(
    byteWidth,
    String(result.stats.bytes).length
  );
}

for (const result of results) {
  const output = [];

  if (!countLines && !countWords && !countBytes) {
    output.push(String(result.stats.lines).padStart(lineWidth));
    output.push(String(result.stats.words).padStart(wordWidth));
    output.push(String(result.stats.bytes).padStart(byteWidth));
  } else {
    if (countLines) {
      output.push(String(result.stats.lines).padStart(lineWidth));
    }

    if (countWords) {
      output.push(String(result.stats.words).padStart(wordWidth));
    }

    if (countBytes) {
      output.push(String(result.stats.bytes).padStart(byteWidth));
    }
  }

  output.push(result.filename);

  console.log(output.join(" "));
}