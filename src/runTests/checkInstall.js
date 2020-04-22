const colors = require('colors');
const commandExists = require('command-exists').sync;
const exec = require("shelljs.exec");
var installed=[];
function checkShell(sh){
  if(commandExists(sh)){
    const reportGood=sh+' is installed!';
    console.log(reportGood.green);
    installed.push(sh);
  }else{
    const reportBad=sh+' is not installed!';
    console.log(reportBad.red);
  };
};
function runScripts(shls, n){
  var output=[];
  for(var s=0; s<shls.length; s++){
    for(var i=1; i<n; i++){
      output.push(shls[s]+' /home/tests/testscripts/script'+n+'.sh');
    }
  }
  return output;
}
function parse(obj){
  console.log(('Stdout: '+obj.stdout).toString().yellow);
  console.log(('Stderr: '+obj.stderr).toString().green);
  console.log(('Exit code: '+obj.code).toString().purple);
}
function main(){
  const shells=['dash', 'yash', 'ksh', 'mksh', 'bosh', 'zsh', 'fish', 'bash3', 'bash4', 'bash5', 'heirloom-sh', 'osh'];
  shells.map(x => checkShell(x));
  var commands=runScripts(installed, 15);
  commands.map(command => parse(exec(command, {silent: true})));
}
main();
