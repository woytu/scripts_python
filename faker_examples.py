#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author : bajins https://www.bajins.com
# @File : faker_examples.py
# @Version: 1.1.0
# @Time : 2020/8/14 15:30
# @Project: scripts_python
# @Package:
# @Software: PyCharm
import sys
# https://faker.readthedocs.io/en/master/locales/en_CA.html
from faker import Faker, Factory

# 生成的地址假数据相互之间无逻辑关系
# https://codertang.com/2020/09/05/python-faker
fake = Faker('en_CA')
# fake = Factory.create(locale='en_CA')

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers".center(100, "="))

# print(fake.bothify(letters='ABCDE')())
print(fake.bothify(text='Product Number: ????-########'))
print(fake.bothify(text='Product Number: ????-########', letters='ABCDE'))
print(fake.hexify(text='MAC Address: ^^:^^:^^:^^:^^:^^'))
print(fake.hexify(text='MAC Address: ^^:^^:^^:^^:^^:^^', upper=True))
print(fake.language_code())
print(fake.lexify(text='Random Identifier: ??????????'))
print(fake.lexify(text='Random Identifier: ??????????', letters='ABCDE'))
print(fake.locale())
print(fake.numerify(text='Intel Core i%-%%##K vs AMD Ryzen % %%##X'))
print(fake.numerify(text='!!! !!@ !@! !@@ @!! @!@ @@! @@@'))
print(fake.random_choices(elements=('a', 'b', 'c', 'd')))
print(fake.random_choices(elements=('a', 'b', 'c', 'd'), length=10))
# print(fake.random_choices(elements=OrderedDict([("a", 0.45), ("b", 0.35), ("c", 0.15), ("d", 0.05), ])))
# print(fake.random_choices(elements=OrderedDict([("a", 0.45), ("b", 0.35), ("c", 0.15), ("d", 0.05), ]), length=20))
print(fake.random_digit())
print(fake.random_digit_not_null())
print(fake.random_digit_not_null_or_empty())
print(fake.random_digit_or_empty())
print(fake.random_element(elements=('a', 'b', 'c', 'd')))
# print(fake.random_element(elements=OrderedDict([("a", 0.45), ("b", 0.35), ("c", 0.15), ("d", 0.05), ])))
print(fake.random_elements(elements=('a', 'b', 'c', 'd'), unique=False))
print(fake.random_elements(elements=('a', 'b', 'c', 'd'), unique=True))
print(fake.random_elements(elements=('a', 'b', 'c', 'd'), length=10, unique=False))
print(fake.random_elements(elements=('a', 'b', 'c', 'd'), length=4, unique=True))
# print(fake.random_elements(elements=OrderedDict([("a", 0.45), ("b", 0.35), ("c", 0.15), ("d", 0.05), ]), length=20, unique=False))
# print(fake.random_elements(elements=OrderedDict([("a", 0.45), ("b", 0.35), ("c", 0.15), ("d", 0.05), ]), unique=True))
print(fake.random_int())
print(fake.random_int(min=0, max=15))
print(fake.random_int(min=0, max=15, step=3))
print(fake.random_letter())
print(fake.random_letters())
print(fake.random_letters(length=10))
print(fake.random_lowercase_letter())
print(fake.random_number(fix_len=False))
print(fake.random_number(fix_len=True))
print(fake.random_number(digits=3))
print(fake.random_number(digits=3, fix_len=False))
print(fake.random_number(digits=3, fix_len=True))
print(fake.random_sample(elements=('a', 'b', 'c', 'd', 'e', 'f')))
print(fake.random_sample(elements=('a', 'b', 'c', 'd', 'e', 'f'), length=3))
print(fake.random_uppercase_letter())
print(fake.randomize_nb_elements(number=100))
print(fake.randomize_nb_elements(number=100, ge=True))
print(fake.randomize_nb_elements(number=100, ge=True, min=120))
print(fake.randomize_nb_elements(number=100, le=True))
print(fake.randomize_nb_elements(number=100, le=True, max=80))
print(fake.randomize_nb_elements(number=79, le=True, ge=True, min=80))

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.address".center(100, "="))

print(fake.address())
print(fake.building_number())
print(fake.city())
print(fake.city_suffix())
print(fake.country())
print(fake.country_code())
print(fake.postcode())
print(fake.street_address())
print(fake.street_name())
print(fake.street_suffix())

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.automotive".center(100, "="))

print(fake.license_plate())

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.bank".center(100, "="))

print(fake.bank_country())
print(fake.bban())
print(fake.iban())

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.barcode".center(100, "="))

print(fake.ean(length=13))
print(fake.ean(length=8))
print(fake.ean13())
print(fake.ean13(leading_zero=False))
print(fake.ean13(leading_zero=True))
print(fake.ean8())
print(fake.upc_a())
print(fake.upc_a(upc_ae_mode=True, number_system_digit=0))
print(fake.upc_a(upc_ae_mode=True, number_system_digit=1))
print(fake.upc_a(upc_ae_mode=True, base='123456', number_system_digit=0))
print(fake.upc_a(upc_ae_mode=True, base='120003', number_system_digit=0))
print(fake.upc_a(upc_ae_mode=True, base='120004', number_system_digit=0))
print(fake.upc_e())
print(fake.upc_e(base='123456'))
print(fake.upc_e(base='123456', number_system_digit=0))
print(fake.upc_e(base='123456', number_system_digit=1))
print(fake.upc_e(base='120000', number_system_digit=0))
print(fake.upc_e(base='120003', number_system_digit=0))
print(fake.upc_e(base='120004', number_system_digit=0))
print(fake.upc_e(base='120000', number_system_digit=0, safe_mode=False))
print(fake.upc_e(base='120003', number_system_digit=0, safe_mode=False))
print(fake.upc_e(base='120004', number_system_digit=0, safe_mode=False))

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.color".center(100, "="))

print(fake.color(hue='red'))
print(fake.color(luminosity='light'))
print(fake.color(hue=(100, 200), color_format='rgb'))
print(fake.color(hue='orange', luminosity='bright'))
print(fake.color(hue=135, luminosity='dark', color_format='hsv'))
print(fake.color(hue=(300, 20), luminosity='random', color_format='hsl'))
print(fake.color_name())
print(fake.hex_color())
print(fake.rgb_color())
print(fake.rgb_css_color())
print(fake.safe_color_name())
print(fake.safe_hex_color())

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.company".center(100, "="))

print(fake.bs())
print(fake.catch_phrase())
print(fake.company())
print(fake.company_suffix())

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.credit_card".center(100, "="))

print(fake.credit_card_expire())
print(fake.credit_card_full())
print(fake.credit_card_number())
print(fake.credit_card_provider())
print(fake.credit_card_security_code())

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.currency".center(100, "="))

print(fake.cryptocurrency())
print(fake.cryptocurrency_code())
print(fake.cryptocurrency_name())
print(fake.currency())
print(fake.currency_code())
print(fake.currency_name())
print(fake.currency_symbol())

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.date_time".center(100, "="))

print(fake.am_pm())
print(fake.century())
print(fake.date())
print(fake.date_between())
print(fake.date_between_dates())
print(fake.date_object())
print(fake.date_of_birth())
print(fake.date_this_century())
print(fake.date_this_decade())
print(fake.date_this_month())
print(fake.date_this_year())
print(fake.date_time())
print(fake.date_time_ad())
print(fake.date_time_between())
print(fake.date_time_between_dates())
print(fake.date_time_this_century())
print(fake.date_time_this_decade())
print(fake.date_time_this_month())
print(fake.date_time_this_year())
print(fake.day_of_month())
print(fake.day_of_week())
print(fake.future_date())
print(fake.future_datetime())
print(fake.iso8601())
print(fake.month())
print(fake.month_name())
print(fake.past_date())
print(fake.past_datetime())
print(fake.time())
print(fake.time_delta())
print(fake.time_object())
print(fake.time_series())
print(fake.timezone())
print(fake.unix_time())
print(fake.year())

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.file".center(100, "="))

print(fake.file_extension())
print(fake.file_name())
print(fake.file_path())
print(fake.mime_type())
print(fake.unix_device())
print(fake.unix_partition())

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.geo".center(100, "="))

print(fake.coordinate())
print(fake.latitude())
print(fake.latlng())
print(fake.local_latlng())
print(fake.location_on_land())
print(fake.longitude())

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.internet".center(100, "="))

print(fake.ascii_company_email())
print(fake.ascii_email())
print(fake.ascii_free_email())
print(fake.ascii_safe_email())
print(fake.company_email())
print(fake.dga())
print(fake.domain_name())
print(fake.domain_word())
print(fake.email())
print(fake.free_email())
print(fake.free_email_domain())
print(fake.hostname())
print(fake.http_method())
print(fake.image_url())
print(fake.ipv4())
print(fake.ipv4_network_class())
print(fake.ipv4_private())
print(fake.ipv4_public())
print(fake.ipv6())
print(fake.mac_address())
print(fake.port_number())
print(fake.safe_email())
print(fake.slug())
print(fake.tld())
print(fake.uri())
print(fake.uri_extension())
print(fake.uri_page())
print(fake.uri_path())
print(fake.url())
print(fake.user_name())

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.isbn".center(100, "="))

print(fake.isbn10())
print(fake.isbn13())

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.job".center(100, "="))

print(fake.job())

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.lorem".center(100, "="))

print(fake.paragraph())
print(fake.paragraphs())
print(fake.sentence())
print(fake.sentences())
print(fake.text())
print(fake.texts())
print(fake.word())
print(fake.words())

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.misc".center(100, "="))

print(fake.binary(length=64))
print(fake.boolean(chance_of_getting_true=25))
print(fake.boolean(chance_of_getting_true=50))
print(fake.boolean(chance_of_getting_true=75))
print(fake.csv(data_columns=('{{name}}', '{{address}}'), num_rows=10, include_row_ids=False))
print(fake.csv(header=('Name', 'Address', 'Favorite Color'),
               data_columns=('{{name}}', '{{address}}', '{{safe_color_name}}'), num_rows=10, include_row_ids=True))
print(fake.dsv(dialect='excel', data_columns=('{{name}}', '{{address}}')))
print(fake.dsv(dialect='excel-tab', data_columns=('{{name}}', '{{address}}'), include_row_ids=True))
print(fake.dsv(data_columns=('{{name}}', '{{address}}'), num_rows=5, delimiter='$'))
print(fake.md5(raw_output=False))
print(fake.md5(raw_output=True))
print(fake.null_boolean())
print(fake.password(length=12))
print(fake.password(length=40, special_chars=False, upper_case=False))
print(fake.psv(data_columns=('{{name}}', '{{address}}'), num_rows=10, include_row_ids=False))
print(fake.psv(header=('Name', 'Address', 'Favorite Color'),
               data_columns=('{{name}}', '{{address}}', '{{safe_color_name}}'), num_rows=10, include_row_ids=True))
print(fake.sha1(raw_output=False))
print(fake.sha1(raw_output=True))
print(fake.sha256(raw_output=False))
print(fake.sha256(raw_output=True))
print(fake.tar(uncompressed_size=256, num_files=4, min_file_size=32))
print(fake.tar(uncompressed_size=256, num_files=32, min_file_size=4, compression='bz2'))
print(fake.tsv(data_columns=('{{name}}', '{{address}}'), num_rows=10, include_row_ids=False))
print(fake.tsv(header=('Name', 'Address', 'Favorite Color'),
               data_columns=('{{name}}', '{{address}}', '{{safe_color_name}}'), num_rows=10, include_row_ids=True))
# print(fake.uuid4())
# print(fake.uuid4(cast_to=None))
print(fake.zip(uncompressed_size=256, num_files=4, min_file_size=32))
print(fake.zip(uncompressed_size=256, num_files=32, min_file_size=4, compression='bz2'))

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.person".center(100, "="))

print(fake.first_name())
print(fake.first_name_female())
print(fake.first_name_male())
print(fake.last_name())
print(fake.last_name_female())
print(fake.last_name_male())
print(fake.name())
print(fake.name_female())
print(fake.name_male())
print(fake.prefix())
print(fake.prefix_female())
print(fake.prefix_male())
print(fake.suffix())
print(fake.suffix_female())
print(fake.suffix_male())

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.phone_number".center(100, "="))

print(fake.country_calling_code())
print(fake.msisdn())
print(fake.phone_number())

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.profile".center(100, "="))

print(fake.profile())
print(fake.simple_profile())

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.python".center(100, "="))

print(fake.pybool())
print(fake.pydecimal())
print(fake.pydict())
print(fake.pyfloat())
print(fake.pyint())
print(fake.pyiterable())
print(fake.pylist())
print(fake.pyset())
print(fake.pystr())
print(fake.pystr_format())
print(fake.pystruct())
print(fake.pytuple())

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.ssn".center(100, "="))

print(fake.ssn())

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "providers.user_agent".center(100, "="))

print(fake.android_platform_token())
print(fake.chrome())
print(fake.firefox())
print(fake.internet_explorer())
print(fake.ios_platform_token())
print(fake.linux_platform_token())
print(fake.linux_processor())
print(fake.mac_platform_token())
print(fake.mac_processor())
print(fake.opera())
print(fake.safari())
print(fake.user_agent())
print(fake.windows_platform_token())

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "Locale en_CA".center(100, "="))

print(fake.address())
print(fake.building_number())
print(fake.city())
print(fake.city_prefix())
print(fake.city_suffix())
print(fake.country())
print(fake.country_code())
print(fake.postal_code_letter())
print(fake.postalcode())
print(fake.postalcode_in_province())
print(fake.postcode())
print(fake.postcode_in_province())
print(fake.province())
print(fake.province_abbr())
print(fake.secondary_address())
print(fake.street_address())
print(fake.street_name())
print(fake.street_suffix())

print("\033[0;31m[%s@%s]\033[0m" % (__file__, sys._getframe().f_lineno), "".center(100, "="))

# print(fake.barcode())
print(fake.color())
# print(fake.credit_card())
# print(fake.file())
# print(fake.geo())
# print(fake.internet())
# print(fake.isbn())
# print(fake.lorem())
# print(fake.misc())
# print(fake.person())
# print(fake.python())
