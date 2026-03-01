import React, { useState, useEffect } from 'react'
import { usePapaParse } from 'react-papaparse'
import { useAuth0 } from "@auth0/auth0-react";
import axios from 'axios'

function FileUpload() {

    const { readString } = usePapaParse();
    const [jsonData, setJsonData] = useState(null);
    const [file, setFile] = useState(null);
    const [fileCheck, setFileCheck] = useState(false);
    const [dataToDisplay, setDataToDisplay] = useState(false);
    const [userResData, setUserResData] = useState(null);
    const [error, setError] = useState(false);

    const { user } = useAuth0();
    const username = user.nickname;

    const fileChange = (e) => {
        setFile(e.target.files[0]);
        setError(false);
    };

    const parseFile = () => {
        if (file) {
            readString(file, {
                header: false,
                complete: (results) => {
                    setJsonData(results.data);
                    setFileCheck(true);
                },
                error: (error) => {
                    console.error('Error parsing CSV:', error);
                },
            });
        }
    }

    useEffect(() => {
        const checkFile = () => {
            let validFile = true;
            const dateRegex = /^\d{4}-\d{2}-\d{2} \d{1,2}:\d{2}:\d{2}$/;
            const intRegex = /^\d+$/
            jsonData.forEach(element => {
                if (!dateRegex.test(element[0]) || !intRegex.test(element[1]) || !intRegex.test(element[2])) {
                    validFile = false;
                }
            });
            if (validFile) {
                processData();
            }
            else {
                setError(true);
            }
        }

        if (fileCheck) {
            checkFile();
            setFileCheck(false);
        }

    }, [fileCheck])

    useEffect(() => {
        setDataToDisplay(true);
        console.log(userResData);
    }, [userResData])

    const processData = () => {
        setDataToDisplay(false);
        axios.post(`http://localhost:5000/uploadcsv/${username}`, { jsonData })
        .then(response => { 
            setUserResData(response.data[0][0]);
        })
        .catch(error => {
            console.error('There was an error processing the data', error);
        })
    }

    return (
        <>
            <div className="d-grid gap-2 col-2 mx-auto p-2 bg-light-subtle bg-gradient mt-4 rounded">
                <span className="text-primary text-center"></span>
                <div className="mb-3">
                    <label htmlFor="csvFile" className="form-label">Traffic Data File</label>
                    <input className="form-control" type="file" accept=".csv" id="csvFile" onChange={fileChange}/>
                </div>
                <button className="btn btn-secondary-subtle b-1" onClick={parseFile} disabled={!file}>
                    Upload CSV
                </button>
                {error && <span className="text-danger text-center">Error: Invalid CSV file</span>}
            </div>
            <div className="d-grid gap-2 col-6 mx-auto p-2 bg-light-subtle bg-gradient mt-4 rounded">
                {dataToDisplay && <div className="d-grid gap-2 col-8 mx-auto p-2 bg-light-subtle bg-gradient mt-4 rounded">
                    {userResData && 
                    <div className="text-center">
                        <h3>Traffic Model Results (Daily)</h3>
                        <p>Daily Average Traffic: {userResData.Daily_Avg}</p>
                        <p>Peak Volume Day: {userResData.Highest_Day}, Peak of: {userResData.HD_val}</p>
                    </div>
                    }
                </div>}
            </div>
        </>
    )
}

export default FileUpload
