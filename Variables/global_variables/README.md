# Global Variables
<!DOCTYPE html>
<html>
<body>
    <ol>
        <li>
            <h2>Global Variables</h2>
            <ul>
                <li>Variables that are created outside of a function (as in all of the examples above) are known as global variables.</li>
                <li>Global variables can be used by everyone, both inside of functions and outside.</li>
                <li>
                    <pre>
                        <code>
                        x = "awesome"
                        def myfunc():
                        print("Python is " + x)
                        myfunc()
                        </code>
                    </pre>
                </li>
                <li>If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.</li>
                <li>
                    <pre>
                        <code>
                            x = "awesome"
                            def myfunc():
                            x = "fantastic"
                            print("Python is " + x)
                            myfunc()
                            print("Python is " + x) 
                        </code>
                    </pre>
                </li>
            </ul>
        </li>
        <li>
            <h2>The global Keyword</h2>
            <ul>
                <li>Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.</li>
                <li>To create a global variable inside a function, you can use the <code>global</code> keyword.</li>
                <li>
                    <pre>
                        <code>
                            x = "awesome"
                            def myfunc():
                            global x
                            x = "fantastic"
                            myfunc()
                            print("Python is " + x)
                        </code>
                    </pre>
                </li>
            </ul>
        </li>
    </ol>
</body>
</html>