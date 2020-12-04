import re


class Passport(dict):
    def __init__(self):
        self.validators = [self.validate_all]

    def validate_all(self):
        attributes = [
            'byr', # (Birth Year)
            'iyr', # (Issue Year)
            'eyr', # (Expiration Year)
            'hgt', # (Height)
            'hcl', # (Hair Color)
            'ecl', # (Eye Color)
            'pid', # (Passport ID)
            # 'cid', # (Country ID)
        ]
        return all((attribute in self for attribute in attributes))

    def isValid(self):
        return all(validator() for validator in self.validators)

def parse_passport_data(data, passport_type=Passport):
    passports = []
    current_passport = None
    for line in data:
        if not line and current_passport:
            passports.append((current_passport, current_passport.isValid()))
        if not current_passport or not line:
            current_passport = passport_type()
        for attr in line.split():
            k, v = attr.split(':')
            current_passport[k] = v
    # Catch the last entry
    passports.append((current_passport, current_passport.isValid()))

    return passports


data = open("day04.input").read().splitlines()

passports = parse_passport_data(data)
print "Part 1: ", len([x for x in passports if x[1]])


class StricterPassport(Passport):
    def __init__(self):
        self.validators = [
            self.valid_byr,
            self.valid_iyr,
            self.valid_eyr,
            self.valid_hgt,
            self.valid_hcl,
            self.valid_ecl,
            self.valid_pid,
        ]

    def valid_byr(self):
        try:
            byr = self['byr']
            return len(byr) == 4 and (1920 <= int(byr) <= 2002)
        except (KeyError, ValueError):
            return False

    def valid_iyr(self):
        try:
            iyr = self['iyr']
            return len(iyr) == 4 and (2010 <= int(iyr) <= 2020)
        except (KeyError, ValueError):
            return False

    def valid_eyr(self):
        try:
            eyr = self['eyr']
            return len(eyr) == 4 and (2020 <= int(eyr) <= 2030)
        except (KeyError, ValueError):
            return False

    def valid_hgt(self):
        try:
            hgt = self['hgt']
            if hgt.endswith('cm'):
                return 150 <= int(hgt[:-2]) <= 193
            elif hgt.endswith('in'):
                return 59 <= int(hgt[:-2]) <= 78
            else:
                return False
        except (KeyError, ValueError):
            return False

    def valid_hcl(self):
        try:
            return bool(re.match(r'^#[0-9a-f0]{6}$', self['hcl']))
        except KeyError:
            return False

    def valid_ecl(self):
        try:
            return self['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        except KeyError:
            return False

    def valid_pid(self):
        try:
            pid = self['pid']
            int(pid)
            return len(pid) == 9
        except (KeyError, ValueError):
            return False

passports2 = parse_passport_data(data, passport_type=StricterPassport)
print "Part 2: ", len([x for x in passports2 if x[1]])
