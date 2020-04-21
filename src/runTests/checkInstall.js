const colors = require('colors');
const commandExists = require('command-exists');
function checkShell(sh){
  commandExists(sh)
  .then(function(){
    const reportGood=sh+' is installed!';
    console.log(reportGood.green);
  }).catch(function(){
    const reportBad=sh+' is not installed!';
    console.log(reportBad.red);
  });
};
const shells=['dash', 'yash', 'ksh', 'mksh', 'bosh', 'zsh', 'fish', 'bash3', 'bash4', 'bash5', 'heirloom-sh', 'osh'];
shells.map(x => checkShell(x));
