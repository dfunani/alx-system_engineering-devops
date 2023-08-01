#!/usr/bin/env ruby
puts ARGV[0].scan(/[(]\d\d\d[)]?[-\s]?\d\d\d[-\s]?\d\d\d\d/).join
