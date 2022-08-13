# create a file in /tmp using puppet
file { '/tmp/school':
ensure  => file,
path    => '/tmp/school',
owner   => 'www-data',
group   => 'www-data',
mode    => '0744',
content => 'I love Puppet',
}