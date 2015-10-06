entities = {
    '.': '&#46;',
    '@': '&#64;',
    '-': '&#45;',
    '_': '&#95;',

    '0': '&#48;',
    '1': '&#49;',
    '2': '&#50;',
    '3': '&#51;',
    '4': '&#52;',
    '5': '&#53;',
    '6': '&#54;',
    '7': '&#55;',
    '8': '&#56;',
    '9': '&#57;',

    'A': '&#65;',
    'B': '&#66;',
    'C': '&#67;',
    'D': '&#68;',
    'E': '&#69;',
    'F': '&#70;',
    'G': '&#71;',
    'H': '&#72;',
    'I': '&#73;',
    'J': '&#74;',
    'K': '&#75;',
    'L': '&#76;',
    'M': '&#77;',
    'N': '&#78;',
    'O': '&#79;',
    'P': '&#80;',
    'Q': '&#81;',
    'R': '&#82;',
    'S': '&#83;',
    'T': '&#84;',
    'U': '&#85;',
    'V': '&#86;',
    'W': '&#87;',
    'X': '&#88;',
    'Y': '&#89;',
    'Z': '&#90;',

    'a': '&#97;',
    'b': '&#98;',
    'c': '&#99;',
    'd': '&#100;',
    'e': '&#101;',
    'f': '&#102;',
    'g': '&#103;',
    'h': '&#104;',
    'i': '&#105;',
    'j': '&#106;',
    'k': '&#107;',
    'l': '&#108;',
    'm': '&#109;',
    'n': '&#110;',
    'o': '&#111;',
    'p': '&#112;',
    'q': '&#113;',
    'r': '&#114;',
    's': '&#115;',
    't': '&#116;',
    'u': '&#117;',
    'v': '&#118;',
    'w': '&#119;',
    'x': '&#120;',
    'y': '&#121;',
    'z': '&#122;',

}

def MailTo(email):

    if '@' not in email:
      email = 'test@test.com'
    if email.split('@').__len__() > 2:
      email = 'test@test.com'

    email = email.split('@')

    uno = ''
    for c in email[0]:
        if c in entities:
            uno += entities[c]
        else:
            uno += c

    dos = ''
    for c in email[1]:
        if c in entities:
            dos += entities[c]
        else:
            dos += c

    #''' <!--- Start HTML --> '''

    html = u"""<script language=Javascript type=text/javascript>
document.write('<a href="mai');
document.write('lto');
document.write(':%s');
document.write('&#64;');
document.write('%s">');
document.write('%s');
document.write('&#64;');
document.write('%s<\/a>');
</script>
<noscript>
%s [@t] 
%s
</noscript>
""" % (uno, dos, uno, dos, uno, dos)

    return html

def text_to_entity(text=''):
    text = '<a href="https://github.com/pr0xmeh"><i class="fa fa-4x fa-github" style="color:#000"></i></a>'
    out = ''

    for char in text:
        if char in entities:
            out += entities[char]
        else:
            out += char

    print(out)

def main():

    import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('email', metavar='email',
                   help='an integer for the accumulator')
    args = parser.parse_args()


    print(MailTo(email = args.email))

if __name__ == '__main__':
    text_to_entity()
    main()
