__addition = 'x := 1 ; y := 1 ; z := x + y'
__addittion_vc = 'z > 5'
addition = (__addition, __addittion_vc)

__condition = 'x := 7 ; if ( x > 5 ) then ( z := 3 ) else ( z := 6 ) '
__condition_vc = 'z < 5'
condition = (__condition, __condition_vc)

__condition2 = 'e := 0 ; x := 2 ; y := 1 ; if ( x > y ) then ( e := 1 ) else ( e := 2 )'
__condition2_vc = '(e < 2) & (e = 1)'
condition2 = (__condition2, __condition2_vc)

__condition3 = 'a := 1 ; if ( a > 2 ) then ( a := 2 ) else ( a := 5 ) ; if ( a > 3 ) then ( a := 4 ) else ( a := 5 )'
__condition3_vc = 'a = 4'
condition3 = (__condition3, __condition3_vc)

__coins3 = 'd := 0 ; x := 1; y := 1 ; z := 1 ;'\
		   ' if ( x > y ) then ( if ( x > z ) then ( d := 1 ) else ( d := 3 ) ) else '\
		   '( if ( y > z ) then ( d := 2 ) else ( d := 3 ) )'
__coins3_vc = 'd = 0'
coins3 = (__coins3, __coins3_vc)

__coins4 = 'd := 0 ; x := 1 ; y := 1 ; z := 1 ; f := 4 ; '\
       'if ( x > y ) then ( if ( x > z ) then ( if ( x > f ) then ( d := 1 ) else ( d := 4 ) ) else '\
	   ' ( if ( z > f ) then ( d := 3 ) else ( d := 4 ) ) ) else ( if ( y > z ) then ( if ( y > f ) then ( d := 2 ) else ( d := 4 ) ) '\
	   'else ( if ( z > f ) then ( d := 3 ) else ( d := 4 ) ) )'
__coins4_vc = 'd = 4'
coins4 = (__coins4, __coins4_vc)

__coins4_2 = 'd := 0 ; x := 2 ; y := 2 ; z := 2 ; f := 2 ; '\
    		 'if ( x + y > z + f ) '\
    		 'then ( if ( x > y ) then ( d := 1 ) else ( d := 2 ) ) '\
     		 'else ( if ( z > f ) then ( d := 3 ) else ( d := 4 ) )'
__coins4_2_vc = 'd = 0'
coins4_2 = (__coins4_2, __coins4_2_vc)

__coins12 = 'x := 0 ; '\
	   		'a := 1 ; b := 1 ; c := 2 ; d := 1 ; e := 1 ; f := 1 ; '\
	   		'g := 1 ; h := 1 ; y := 1 ; j := 1 ; k := 1 ; l := 1 ; '\
	   		\
	   		'if ( a + b + c + d + e + f > g + h + y + j + k + l ) '\
	      	   'then ( '\
	              'if ( a + b + c > d + e + f ) '\
	                   'then ( '\
	                      'if ( a > b ) '\
	                         'then ( if ( a > c ) then ( x := 1 ) else ( x := 3 ) ) '\
	                         'else ( if ( b > c ) then ( x := 2 ) else ( x := 3 ) ) '\
	                   ') '\
	                   'else ( '\
	                      'if ( d > e ) '\
	                         'then ( if ( d > f ) then ( x := 4 ) else ( x := 6 ) ) '\
	                         'else ( if ( e > f ) then ( x := 5 ) else ( x := 6 ) ) '\
	                   ') '\
	           ') '\
	      	   'else ( '\
	              'if ( g + h + y > j + k + l ) '\
	                 'then ( '\
	                    'if ( g > h ) '\
	                       'then ( if ( g > y ) then ( x := 7 ) else ( x := 9 ) ) '\
	                       'else ( if ( h > y ) then ( x := 8 ) else ( x := 9 ) ) '\
	                  ') '\
	              'else ( '\
	                   'if ( j > k ) '\
	                      'then ( if ( j > l ) then ( x := 10 ) else ( x := 12 ) ) '\
	                      'else ( if ( k > l ) then ( x := 11 ) else ( x := 12 ) ) '\
	              ') '\
	      ') '
__coins12_vc = '(x > 0) & (x < 4)'
# 4 comparison
coins12 = (__coins12, __coins12_vc)

__coins15 = 'x := 0 ; '\
	  		'a := 1 ; b := 2 ; c := 1 ; d := 1 ; e := 1 ; f := 1 ; g := 1 ; '\
	   		'h := 1 ; y := 1 ; j := 1 ; k := 1 ; l := 1 ; m := 1 ; n := 1 ; '\
	   		'o := 1 ; '\
	   		\
	   'if ( a + b + c + d + e + f + g > h + y + j + k + l + m + n ) '\
	      'then ( '\
	           'if ( a + b + c > d + e + f ) '\
	              'then ( '\
	                   'if ( a + b > g + o ) '\
	                      'then ( '\
	                           'if ( a > b ) '\
	                              'then ( if ( a > c ) then ( x := 1 ) else ( x := 3 ) ) '\
	                              'else ( if ( b > c ) then ( x := 2 ) else ( x := 3 ) ) '\
	                      ') '\
	                      'else ( '\
	                           'if ( g > o ) '\
	                              'then ( if ( g > c ) then ( x := 7 ) else ( x := 3 ) ) '\
	                              'else ( if ( o > c ) then ( x := 15 ) else ( x := 3 ) ) '\
	                      ') '\
	              ') '\
	              'else ( '\
	                   'if ( d + e > g + o ) '\
	                      'then ( '\
	                           'if ( d > e ) '\
	                              'then ( if ( d > f ) then ( x := 4 ) else ( x := 6 ) ) '\
	                              'else ( if ( e > f ) then ( x := 5 ) else ( x := 6 ) ) '\
	                      ') '\
	                      'else ( '\
	                           'if ( g > o ) '\
	                              'then ( if ( g > f ) then ( x := 7 ) else ( x := 6 ) ) '\
	                              'else ( if ( o > f ) then ( x := 15 ) else ( x := 6 ) ) '\
	                      ') '\
	              ') '\
	      ') '\
	      'else ( '\
	           'if ( h + y + j > k + l + m ) '\
	              'then ( '\
	                   'if ( h + y > n + o ) '\
	                      'then ( '\
	                           'if ( h > y ) '\
	                              'then ( if ( h > j ) then ( x := 8 ) else ( x := 10 ) ) '\
	                              'else ( if ( y > j ) then ( x := 9 ) else ( x := 10 ) ) '\
	                      ') '\
	                      'else ( '\
	                           'if ( n > o ) '\
	                              'then ( if ( n > j ) then ( x := 14 ) else ( x := 10 ) ) '\
	                              'else ( if ( o > j ) then ( x := 15 ) else ( x := 10 ) ) '\
	                      ') '\
	              ') '\
	              'else ( '\
	                   'if ( k + l > n + o ) '\
	                      'then ( '\
	                           'if ( k > l ) '\
	                              'then ( if ( k > m ) then ( x := 11 ) else ( x := 13 ) ) '\
	                              'else ( if ( l > m ) then ( x := 12 ) else ( x := 13 ) ) '\
	                      ') '\
	                      'else ( '\
	                           'if ( n > o ) '\
	                              'then ( if ( n > m ) then ( x := 14 ) else ( x := 13 ) ) '\
	                              'else ( if ( o > m ) then ( x := 15 ) else ( x := 13 ) ) '\
	                      ') '\
	              ') '\
	      ') '
__coins15_vc = 'x = 2'
# 5 comparison
coins15 = (__coins15, __coins15_vc)
