#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(.+)\] \[to:([+]?\d+)\] \[flags:(-?\d:-?\d:-?\d:-?\d:-?\d)\]/).join(",")
