import React, { useState } from 'react';
import Expense from './api/Expense';
import Button from './api/RefreshButton';

const App = () => {
    const [data, setData] = useState(null);
    return (
        <div>
            <Expense 
            setData = {setData}
            data = {data} />
            <Button  />
        </div>
    );
};

export default App;