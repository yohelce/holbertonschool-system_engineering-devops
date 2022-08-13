#Manifest that kills a process named killmenow
exec { 'killmenow':
command  => 'pkill -x killmenow',
provider => 'shell',
user     => 'root',
}
