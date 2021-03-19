from name_that_hash import runner
import click.testing


def test_it_works():

    hashes = ["5d41402abc4b2a76b9719d911017c592"]

    x = runner.api_return_hashes_as_json(hashes)
    assert x is not None


def test_it_identifieis_correctly():
    hashes = ["5d41402abc4b2a76b9719d911017c592"]

    x = runner.api_return_hashes_as_json(hashes)
    assert "NTLM" in x


def test_main_succeeds():
    runn = click.testing.CliRunner()
    result = runn.invoke(runner.main)
    assert result.exit_code == 0


def test_if_no_hashes_found():
    hashes = ["abc"]

    x = runner.api_return_hashes_as_json(hashes)
    assert "[]" in x


def test_bcrypt_dollar():
    # for issue #23
    hashes = ["$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom"]

    x = runner.api_return_hashes_as_json(hashes)
    assert "bcrypt" in x


def test_base64_works():
    # for issue #23
    hashes = ["NWY0ZGNjM2I1YWE3NjVkNjFkODMyN2RlYjg4MmNmOTk="]

    x = runner.api_return_hashes_as_json(hashes, {"base64": True})
    assert "MD5" in x


def test_scrypt_succeeds():
    # for issue #23
    hashes = [
        "SCRYPT:1024:1:1:MDIwMzMwNTQwNDQyNQ==:5FW+zWivLxgCWj7qLiQbeC8zaNQ+qdO0NUinvqyFcfo="
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "scrypt" in x


def test_kerberos1():
    hashes = [
        "$krb5pa$23$user$realm$salt$4e751db65422b2117f7eac7b721932dc8aa0d9966785ecd958f971f622bf5c42dc0c70b532363138363631363132333238383835"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Kerberos 5 AS-REQ Pre-Auth" in x

def test_kerberos2():
    hashes = [
        "$krb5tgs$23$*user$realm$test/spn*$63386d22d359fe42230300d56852c9eb$891ad31d09ab89c6b3b8c5e5de6c06a7f49fd559d7a9a3c32576c8fedf705376cea582ab5938f7fc8bc741acf05c5990741b36ef4311fe3562a41b70a4ec6ecba849905f2385bb3799d92499909658c7287c49160276bca0006c350b0db4fd387adc27c01e9e9ad0c20ed53a7e6356dee2452e35eca2a6a1d1432796fc5c19d068978df74d3d0baf35c77de12456bf1144b6a750d11f55805f5a16ece2975246e2d026dce997fba34ac8757312e9e4e6272de35e20d52fb668c5ed"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Kerberos 5 TGS-REP etype 23" in x

def test_kerberos3():
    hashes = [
        "$krb5asrep$23$user@domain.com:3e156ada591263b8aab0965f5aebd837$007497cb51b6c8116d6407a782ea0e1c5402b17db7afa6b05a6d30ed164a9933c754d720e279c6c573679bd27128fe77e5fea1f72334c1193c8ff0b370fadc6368bf2d49bbfdba4c5dccab95e8c8ebfdc75f438a0797dbfb2f8a1a5f4c423f9bfc1fea483342a11bd56a216f4d5158ccc4b224b52894fadfba3957dfe4b6b8f5f9f9fe422811a314768673e0c924340b8ccb84775ce9defaa3baa0910b676ad0036d13032b0dd94e3b13903cc738a7b6d00b0b3c210d1f972a6c7cae9bd3c959acf7565be528fc179118f28c679f6deeee1456f0781eb8154e18e49cb27b64bf74cd7112a0ebae2102ac"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Kerberos 5 AS-REP etype 23" in x

def test_kerberos4():
    hashes = [
        "$krb5tgs$17$user$realm$ae8434177efd09be5bc2eff8$90b4ce5b266821adc26c64f71958a475cf9348fce65096190be04f8430c4e0d554c86dd7ad29c275f9e8f15d2dab4565a3d6e21e449dc2f88e52ea0402c7170ba74f4af037c5d7f8db6d53018a564ab590fc23aa1134788bcc4a55f69ec13c0a083291a96b41bffb978f5a160b7edc828382d11aacd89b5a1bfa710b0e591b190bff9062eace4d26187777db358e70efd26df9c9312dbeef20b1ee0d823d4e71b8f1d00d91ea017459c27c32dc20e451ea6278be63cdd512ce656357c942b95438228e"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Kerberos 5 TGS-REP etype 17 (AES128-CTS-HMAC-SHA1-96)" in x

def test_kerberos5():
    hashes = [
        "$krb5tgs$18$user$realm$8efd91bb01cc69dd07e46009$7352410d6aafd72c64972a66058b02aa1c28ac580ba41137d5a170467f06f17faf5dfb3f95ecf4fad74821fdc7e63a3195573f45f962f86942cb24255e544ad8d05178d560f683a3f59ce94e82c8e724a3af0160be549b472dd83e6b80733ad349973885e9082617294c6cbbea92349671883eaf068d7f5dcfc0405d97fda27435082b82b24f3be27f06c19354bf32066933312c770424eb6143674756243c1bde78ee3294792dcc49008a1b54f32ec5d5695f899946d42a67ce2fb1c227cb1d2004c0"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Kerberos 5 TGS-REP etype 18 (AES256-CTS-HMAC-SHA1-96)" in x

def test_kerberos6():
    hashes = [
         "$krb5pa$17$hashcat$HASHCATDOMAIN.COM$a17776abe5383236c58582f515843e029ecbff43706d177651b7b6cdb2713b17597ddb35b1c9c470c281589fd1d51cca125414d19e40e333"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Kerberos 5, etype 17, Pre-Auth" in x

def test_kerberos7():
    hashes = [
        "$krb5pa$17$user1$EXAMPLE.COM$$c5461873dc13665771b98ba80be53939e906d90ae1ba79cf2e21f0395e50ee56379fbef4d0298cfccfd6cf8f907329120048fd05e8ae5df4"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Kerberos 5, etype 17, Pre-Auth (with salt)" in x

def test_kerberos8():
    hashes = [
        "$krb5pa$18$hashcat$HASHCATDOMAIN.COM$96c289009b05181bfd32062962740b1b1ce5f74eb12e0266cde74e81094661addab08c0c1a178882c91a0ed89ae4e0e68d2820b9cce69770"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Kerberos 5, etype 18, Pre-Auth" in x
    
    
def test_scrypt_python_dict():
    # for issue #23
    hashes = [
        "SCRYPT:1024:1:1:MDIwMzMwNTQwNDQyNQ==:5FW+zWivLxgCWj7qLiQbeC8zaNQ+qdO0NUinvqyFcfo="
    ]

    x = runner.api_return_hashes_as_dict(hashes)
    assert "SCRYPT:1024:1:1:MDIwMzMwNTQwNDQyNQ==:5FW+zWivLxgCWj7qLiQbeC8zaNQ+qdO0NUinvqyFcfo=" in x

def test_etherum():
    # for issue #23
    hashes = [
        "$ethereum$p*262144*3238383137313130353438343737383736323437353437383831373034343735*06eae7ee0a4b9e8abc02c9990e3730827396e8531558ed15bb733faf12a44ce1*e6d5891d4f199d31ec434fe25d9ecc2530716bc3b36d5bdbc1fab7685dda3946"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Ethereum" in x

def test_bitcoin():
    # for issue #23
    hashes = [
        "$bitcoin$96$d011a1b6a8d675b7a36d0cd2efaca32a9f8dc1d57d6d01a58399ea04e703e8bbb44899039326f7a00f171a7bbc854a54$16$1563277210780230$158555$96$628835426818227243334570448571536352510740823233055715845322741625407685873076027233865346542174$66$625882875480513751851333441623702852811440775888122046360561760525"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Bitcoin / Litecoin" in x

def test_monero():
    # for issue #23
    hashes = [
        "$monero$0*dbaa1db887689e76af0c5a8a7d71595983843c58bca382192e477262d820a98fcd12955335171a96670f8282d09ad4dc67bb66b3fc0590b028d53e574ef908d97cac8578878a6147112dff92cc322e8d86b34e96807f70f5ede43254454bdfe2c6216280d181b495ae24f49ab1aaaebaec4f856f3d160f1d2176b79dd6eb64fa3e192ecfa054be5bbb780364f7c444f23d62fba00d1e125b8b12e518102a48f8c4f7bcba2ca7fefe4e0acd0b61352e32bc821bcbbe211ce433204c08aced7766cfc20b5b2538ef269a91fc5e96d214a8b9cb9bc7c1cc87279164d64353450daaf4f2f8b964f051111ea49a9fbf358e8746cdf043460b975a1eb59e02f3960ab92b59ae5161158d4d0f4c982a4e744b7bcd0319210073ff17a8ca433bd4ff8fe0907882bc43371775ad2ad1beb0c551cebfb4ff9b0dae57d25ea530e5976f874e22a25ad8b79007ee89c9e1923e016f39bc1cd16ac1e34984a2e786896d235a7900a127acc1cf33cebdfba171eb2a36924363d86d98c29c93666ac7a779dfec08f87632fa1b25250ff93ba300b166618cfdd2415b8b3075a431cd785bc22846329111fcbd230375e8c145c76721e65e801948c756f7519add6b6f3ef82bd92f10c47a6d1c5cd45a196fb3a9345186ed1b676de850940ca735f5e81f74df8f54ae906f916b847cf666b74d3632cba2d8f6a2ae8eb8ff34ff1ede7d9a602026cf1f1392ab24491a14983875fd3a4eb2e93caa4de867fd78b1853af9134d866a2abf70a8ef13ada0cb0f49cefe622393219c6a54eaedf37673f1c09af47f884db063d432021a27cff463ef6bb90c9fa5db884b0673c7681eea38b17eb503dba448b406d27f76eaab7693a60ba5bb376167e25d9d37e44c0fc49a20cf082100697a7b053f85650d6515359fa0a9ed0b16c7ae2a699e82872487c54734b23a51b0811d18ea270008ac3634c8655d8c662efc6420c0d1d890e97a457924eb7f148c519955fd7bfcb319ae49bc64ac6fa9beba327b029116afeee7d1002c24c16e163cd15ccc7a964326e881c6b3085abfd49c253946bbacfd5eeb979365690fb281501bf1e88359f630cdff78244160fb129b8b2610e24ca117b74d9a4b2fcdbed0f59e9d71109d9b93661be7408ebd7aa3c7360bb0069eb553e5ee808b08aa330f9a91f1fa9075c1a1817dd0a4c06be756122597044a43a3b8b5722b169da0b97c8647ae478440f1ad588faf595f573d26e7e66110d70cbe78ef5efeab333f896daa04c3cd222dbfc705b5ab5b10ce46cca036ec4904e786ac91eb099fb2bc5a6d5b4492d6ec0d07e71c68ac6c2da39794e070f6454a4c4e2678dc9ece69785d4d3ae101f6ad0781b8a515a5059663ebd3a17c4bf5fa4dd56d6fbf387d4e7de3baef9e6da46e9a9ada6155514a29d30e1b334c892c9ad14c49cf63baf66cb2b12725c898e4ba6fc73939872b60c60976285d3727900a0b346d3ccf5bbd1c724daa98f4db3681f41f45d01e8022ca50b812269bf77f4d5d2ed2327d39d7e6d945907513604e1b42ffa88f2414952dbbe7cabdb8b9a14d95d832f455dd1affd16ddacc21d9a9bb9ea69a61e5d7a4df0db6eb7e11736f0955d096bb648ec5de392d57f80d60bfd139992f84cd3622faea5d77dd52ac16932f1d2dae353134ab195e5dc0af5c270553c6a09d11f6d95463ef5de483e529aa88644aaf709ba23f54309e5e9eed235017d674d1a5b11a2e189ea427dbe9151fbe78cc4a34644203ea424fc3016653a5e1d7c265df5a9f37ac5c67a04e0ed0f7df76fa4fd071b49cc7c5f08f80b4766a9b5359310f7efe7a5a694d1d5f875f0bb9367324f32736a84b02e1c042e4c016fc329522f7c31555c6b989ef43a9044474d99c58244d010ac6625be314ceb6e78a4bd3da98f106048d1b5f1fe34bef2edd7194f3e4ad3f6dc9cea7361a4817fbe78b99d0aa0db3dc8ce2299ba9049eed66f70f4feb6e69dfc7a7e7577d6559866abee9652ab6ef89009256105612a4a2b79fd11c55850e1b3c174137436d5c0baa2631db2911202e593b7d0f1d381f2f250fd732a98297dcc20a9a0c1a2c5b98d1482c182bb8d6c22f7cf9f400fd794ca8a1f58e0e790b34f168c39f0f514b918a0856d0621a66a83efc12fc3510ef1a833dc4147ebf23a1347d32355f085dcb0ab0d0206a3fa8858475391b5b47e24b4842c28c0e74044a190ae295aa305deb3dac453837bdcfac52ddd607564ddfd9fb76ee59f4ba"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Monero" in x

def test_dogecoin():
    # for issue #23
    hashes = [
        "DANHz6EQVoWyZ9rER56DwTXHWUxfkv9k2o"
    ]

    x = runner.api_return_hashes_as_json(hashes)
    assert "Dogecoin" in x
