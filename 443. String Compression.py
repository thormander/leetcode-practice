class Solution:
    def compress(self, chars: List[str]) -> int:
        p_group = 0
        write = 0

        while p_group < len(chars):
            count = 1 # amount chars in the same group
            
            # advance p_group to end of repeating characters
            while (p_group + count < len(chars)) and (chars[p_group] == chars[p_group+count]):
                count += 1
                # increment count to make sure we are count same chars

            # write current char at write
            chars[write] = chars[p_group]
            write += 1
            
            # add the number
            if count > 1:
                for num in str(count):
                    chars[write] = num
                    write += 1
            
            p_group += count # set p_group after the subsequent chars
        
        return write
            



'''
  p
              w 
["a","1","2","b","c","c","c"]

count = 12



p stays at begging, count tracks how long repeating chars are

update p at end by doing p + group size

'''
