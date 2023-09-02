# Python Casting
<!DOCTYPE html>
<html>
<body>
    <ol>
        <li>
            <h2>Python Casting</h2>
            <p>There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.</p>
            <p>Casting in Python is therefore done using constructor functions:</p>
            <ul>
                <li><code>int()</code> - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)</li>
                <li><code>float()</code> - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)</li>
                <li><code>str()</code>  - constructs a string from a wide variety of data types, including strings, integer literals and float literals</li>
                <h4>Example.</h4>
                <p>Integers: </p>
                <ul>
                    <li>
                        <pre>
                            <code>
                                x = int(1)   # x will be 1
                                y = int(2.8) # y will be 2
                                z = int("3") # z will be 3
                            </code>
                        </pre>
                    </li>
                </ul>
                <p>Floats: </p>
                <ul>
                    <li>
                        <pre>
                            <code>
                                x = float(1)     # x will be 1.0
                                y = float(2.8)   # y will be 2.8
                                z = float("3")   # z will be 3.0
                                w = float("4.2") # w will be 4.2
                            </code>
                        </pre>
                    </li>
                </ul>
                <p>Strings: </p>
                <ul>
                    <li>
                        <pre>
                            <code>
                                x = str("s1") # x will be 's1'
                                y = str(2)    # y will be '2'
                                z = str(3.0)  # z will be '3.0' 
                            </code>
                        </pre>
                    </li>
                </ul>
            </ul>
        </li>
    </ol>
</body>
</html>