# Kill a proccess
exec { 'pkill killmenow' :
  command => '/usr/bin/pkill killmenow'
}
