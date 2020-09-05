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

function main(){
  const shells=['dash', 'yash', 'ksh', 'mksh', 'bosh', 'zsh', 'fish', 'bash3', 'bash4', 'bash5', 'heirloom-sh', 'osh', 'bash', 'tcsh'];
  shells.map(x => checkShell(x));
}
main();
