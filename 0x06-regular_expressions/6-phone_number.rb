#!/usr/bin/env ruby

puts ARGV[0].scan(/\d\d\d[\s-]{0,1}\d\d\d[\s.]{0,1}\d\d\d\d/).join
