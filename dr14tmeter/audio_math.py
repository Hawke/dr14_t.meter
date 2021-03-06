# dr14_t.meter: compute the DR14 value of the given audiofiles
# Copyright (C) 2011  Simone Riva
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from numpy  import *
import math
import numpy


def dr_rms( y ) :
    n = y.shape
    rms = numpy.sqrt( 2 * numpy.sum( y**2.0 , 0 ) / float(n[0]) )
    return rms

def u_rms( y ) :
    n = y.shape
    rms = numpy.sqrt( numpy.sum( y**2.0 , 0 ) / float(n[0]) )
    return rms

def __u_rms( y ) :
    n = y.shape
    
    samples_per_block = int(1e5)
    blk_cnt = int( n[0] / samples_per_block )
    
    s_sum = numpy.array([0.0,0.0])
    
    curr_sam = 0 
    for i in range( 0 , blk_cnt ):
        r = arange( curr_sam , curr_sam + samples_per_block )
        s_sum = s_sum + numpy.sum( y[r,:]**2.0 , 0 )
        curr_sam = curr_sam + samples_per_block
       
    r = arange( curr_sam , n[0] )
    s_sum = s_sum + numpy.sum( y[r,:]**2.0 , 0 )
     
    rms = numpy.sqrt( s_sum / float(n[0]) )
    return rms


def decibel_u( y , ref ) :
    return 20 * numpy.log10( y / ref )


def decibel_p( y , ref ) :
    return 10 * numpy.log10( y / ref )
    
def audio_min() :
    return 1.0/(2.0**24)

def audio_min16():
    return 1.0/(2.0**16)