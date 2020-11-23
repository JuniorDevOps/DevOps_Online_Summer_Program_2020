def get_reply(number):
    if number%5==0 and number%3==0:
        return 'FizzBuzz'
    elif number%3==0:
        return 'Fizz'
    elif number%5==0:
        return 'Buzz'
    else:
        return ''

def fizzbuzz(n):
    result = []
    result_full = []
    for x in range(1, n+1):
        if get_reply(x) == 'FizzBuzz':
            result.append('FizzBuzz')
            result_full.append('FizzBuzz')
        elif get_reply(x) == 'Fizz':
            result.append('Fizz')
            result_full.append('Fizz')
        elif get_reply(x) == 'Buzz':
            result.append('Buzz')
            result_full.append('Buzz')
        else:
            result_full.append(str(x))
    return [result, result_full]

def main(n):
    print(' | '.join(fizzbuzz(n)[0]))
    print('\n')
    print(' | '.join(fizzbuzz(n)[1]))
    
main(100)


