const colors = require('colors');
const commandExists = require('command-exists').sync;
const exec = require("shelljs.exec");
var readline = require('readline');
var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});
rl.on('line', function(line){
    
})
var installed = [];
function checkShell(sh){
  if(commandExists(sh)){
    installed.push(sh);
  }
};
function runScripts(shls, n){
  var output=[];
  for(var s=0; s<shls.length; s++){
    for(var i=1; i<n; i++){
      output.push(shls[s]+' /home/tests/testscripts/script'+i+'.sh');
    }
  }
  return output;
}
function parse(obj){
  console.log(('Stdout: '+obj.stdout).green);
  console.log(('Stderr: '+obj.stderr).green);
  console.log(('Exit code: '+obj.code).green);
}
function main(){
  const shells=['dash', 'yash', 'ksh', 'mksh', 'bosh', 'zsh', 'fish', 'bash3', 'bash4', 'bash5', 'heirloom-sh', 'osh', 'bash', 'tcsh', 'posh'];
  shells.map(x => checkShell(x));
  var commands=runScripts(installed, 5);
  commands.map(function(command){
    console.log(command.blue);
    parse(exec(command, {silent: true}));
  });
}
main();
