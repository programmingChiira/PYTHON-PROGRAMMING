# Python - Access List Items
<!DOCTYPE html>
<html>
<body>
    <ol>
        <li>
            <h2>Access Items</h2>
            <ul>
                <li>List items are indexed and you can access them by referring to the index number:</li>
            </ul>
        </li>
        <li>
            <h2>Negative Indexing</h2>
            <ul>
                <li>Negative indexing means to start from the end -1 refers to the last item, -2 refers to the second last item etc.</li>
            </ul>
        </li>
        <li>
            <h2>Range of Indexes</h2>
            <ul>
                <li>You can specify a range of indexes by specifying where to start and where to end the range.</li>
                <li>When specifying a range, the return value will be a new list with the specified items.</li>
                <li>Note: The search will start at index 2 (included) and end at index 5 (not included).</li>
                <li>Remember that the first item has index 0.</li>
            </ul>
        </li>
        <li>
            <h2>Range of Negative Indexes</h2>
            <ul>
                <li>Negative indexing means to start from the end -1 refers to the last item, -2 refers to the second last item etc.</li>
                <h4>Example</h4>
                <p>This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):</p>
                <li>
                    <pre>
                        <code>
                            thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
                            print(thislist[-4:-1])
                        </code>
                    </pre>
                </li>
            </ul>
        </li>
        <li>
            <h2>Check if Item Exists</h2>
            <ul>
                <li>To determine if a specified item is present in a list use the <code>in</code> keyword:</li>
            </ul>
        </li>
    </ol>
</body>
</html>
