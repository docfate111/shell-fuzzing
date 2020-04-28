const colors = require('colors');
const commandExists = require('command-exists').sync;
const exec = require("shelljs.exec");
var installed=[];
function checkShell(sh){
  if(commandExists(sh)){
    installed.push(sh);
  }
};
function runScripts(shls){
  var output=[];
  for(var s=0; s<shls.length; s++){
    for(var t=2; t<process.argv.length; t++){
          output.push(shls[s]+' '+process.argv[t]);
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
  if(process.argv.length<3){
    console.log('Usage: '+process.argv[0]+' '+process.argv[1]+' [ shell script ]');
    process.exit();
  }
  const shells=['dash', 'yash', 'ksh', 'mksh', 'bosh', 'zsh', 'fish', 'bash3', 'bash4', 'bash5', 'heirloom-sh', 'osh', 'bash'];
  shells.map(x => checkShell(x));
  var commands=runScripts(installed);
  commands.map(function(command){
    console.log(command.blue);
    parse(exec(command, {silent: true}));
  });
}
main();
