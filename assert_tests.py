from app import to_bin_str
from app import to_oct_str
from app import to_hex_str

if __name__ == "__main__":
    assert to_bin_str(2) == '10'
    assert to_oct_str(8) == '10'
    assert to_hex_str(16) == '10'
    print("Asserts is ok")