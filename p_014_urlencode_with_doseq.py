# `doseq` オプションを使用した `urlencode` の利用: `urlencode` 関数は辞書型データをURLエンコードされたクエリ文字列に変換します。
# `doseq=True` を指定することで、リストやタプル内の各要素が個別のキーと値のペアとしてエンコードされます。
# 例では、`{'key1': ['value1', 'value2'], 'key2': 'value3'}` が `key1=value1&key1=value2&key2=value3` に変換されます。
#
# Using `urlencode` with `doseq`: The `urlencode` function converts dictionary data into a URL-encoded query string.
# By specifying `doseq=True`, each element within lists or tuples is encoded as separate key-value pairs.
# In the example, `{'key1': ['value1', 'value2'], 'key2': 'value3'}` is converted to `key1=value1&key1=value2&key2=value3`.

from urllib import parse

# Example dictionary data
data = {"key1": ["value1", "value2"], "key2": "value3"}

# Convert dictionary to URL-encoded query string with doseq=True
encoded_data = parse.urlencode(data, doseq=True)

# Print the encoded data
print(encoded_data)
# Outputs: key1=value1&key1=value2&key2=value3

# Example: Book Management System - Encode book search parameters

# Sample search parameters
search_params = {
    "title": "1984",
    "authors": ["George Orwell", "Eric Arthur Blair"],
    "genre": "Dystopian",
}

# Encode the search parameters for URL
encoded_search_params = parse.urlencode(search_params, doseq=True)

# Print the encoded search parameters
print(encoded_search_params)
# Outputs: title=1984&authors=George+Orwell&authors=Eric+Arthur+Blair&genre=Dystopian
