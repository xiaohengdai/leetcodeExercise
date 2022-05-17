import csv, os, getopt, sys, random_names

def run_main(output_vcard_num, output_file_name):
    for i in range(output_vcard_num):
        first_name   = random_names.First()
        last_name    = random_names.Last()
        email        = 'iforvert@gmail.com'
        phone_number = random_names.CreatePhone()
        vcf_file = f'{output_file_name}'
        tips = "正在为您生成第 %d 条通讯录。。。" % (i+1)
        print(f'{tips}')
        vcard = make_vcard(first_name, last_name, phone_number)
        append_multiple_lines(vcf_file, vcard)
    print("任务执行完毕！")

def make_vcard(
        first_name,
        last_name,
        phone):
    return [
        'BEGIN:VCARD',
        'VERSION:3.0',
        'PRODID:-//Apple Inc.//iOS 10.3.1//EN',
        f'N:{last_name};{first_name}',
        f'FN:{first_name} {last_name}',
        f'item1.TEL;type=pref:{phone}',
        'item1.X-ABLabel:手机',
        'REV:2017-04-14T05:11:01Z',
        'END:VCARD'
    ]

def write_vcard(f, vcard):
    with open(f, 'w') as f:
        f.writelines([l + '\n' for l in vcard])


def append_multiple_lines(file_name, lines_to_append):
    with open(file_name, "a+") as file_object:
        appendEOL = False
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            appendEOL = True
        for line in lines_to_append:
            if appendEOL == True:
                file_object.write("\n")
            else:
                appendEOL = True
            file_object.write(line)

def main(argv):
    output_file_name = 'faker_vcard.vcf'
    output_vcard_num = 200
    try:
        opts, args = getopt.getopt(argv,"hc:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ('make-vcard.py -o <output_file_name> -c <vcard_count>')
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print ('make-vcard.py -o <output_file_name> -c <vcard_count>')
            sys.exit()
        elif opt in ("-o", "--ofile"):
            output_file_name = arg
        elif opt in ("-c", "--count"):
            output_vcard_num = int(arg)
    
    tips = "即将为您生成 %d 条通讯录到文件 %s" % (output_vcard_num, output_file_name)
    print(tips)
    run_main(output_vcard_num, output_file_name)

if __name__ == "__main__":
   main(sys.argv[1:])