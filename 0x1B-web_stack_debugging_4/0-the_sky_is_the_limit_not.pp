# Solve the request problem
exec { 'Enlarge the number of documents manage by workers':
command => 'sed -i \'$ s/15/1000/\' /etc/default/nginx && /usr/sbin/service nginx restart',
path    => '/usr/bin/:/bin/'
}
