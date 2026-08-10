const fs = require("fs");
const pathModule = require("path");

const args = process.argv.slice(2);

let paths = [];
let onePerLine = false;
let showHidden = false;

for (const arg of args) {
  if (arg === "-1") {
    onePerLine = true;
  } else if (arg === "-a") {
    showHidden = true;
  } else {
    paths.push(arg);
  }
}

if (paths.length === 0) {
  paths.push(".");
}

function listDirectory(dir) {
  let items = fs.readdirSync(dir);

  if (showHidden) {
    items.unshift(".", "..");
  } else {
    items = items.filter(item => !item.startsWith("."));
  }

  if (mode === "onePerLine") {
    items.forEach(console.log);
  } else {
    console.log(items.join("  "));
  }
}

function expandWildcard(input) {
  if (!input.includes("*")) {
    return [input];
  }
  const dir = pathModule.dirname(input);
  const pattern = pathModule.basename(input);
  const files = fs.readdirSync(dir);

  return files
    .filter(file => {
      if (pattern === "*") {
        return showHidden || !file.startsWith(".");
      }

      return file === pattern;
    })
    .map(file => pathModule.join(dir, file));
}

for (const originalPath of paths) {

  const expandedPaths = expandWildcard(originalPath);

  for (const currentPath of expandedPaths) {

    const info = fs.statSync(currentPath);

    if (info.isDirectory()) {
      listDirectory(currentPath);
    }

    else if (info.isFile()) {
      console.log(pathModule.basename(currentPath));
    }

  }

}