import React, { useState } from 'react';
import axios from 'axios';
import ReactPaginate from 'react-paginate';
import './App.css';

function App() {
  const [selectedCompany, setSelectedCompany] = useState('');
  const [responseData, setResponseData] = useState(null);
  const [error, setError] = useState('');
  const [currentPage, setCurrentPage] = useState(0);
  const itemsPerPage = 10; // Number of items per page

  const companies = [
    'Netflix',
    'Nvidia',
    'Crowdstrike',
    'Cloudflare',
    'Strava'
  ];

  const handleResearch = async () => {
    if (!selectedCompany) {
      setError('Please select a company.');
      return;
    }

    try {
      const response = await axios.post('http://localhost:8080/research/', {
        company: selectedCompany,
      }, {
        timeout: 3000000,
      });
      if (response.status === 200) {
        setResponseData(response.data.response.split('\n'));
        setError('');
      } else {
        setError(`Request failed: ${response.statusText}`);
      }
    } catch (error) {
      setError(`An error occurred: ${error.message}`);
    }
  };

  const handlePageClick = ({ selected }) => {
    setCurrentPage(selected);
  };

  const pageCount = responseData ? Math.ceil(responseData.length / itemsPerPage) : 0;
  const displayItems = responseData
    ? responseData.slice(currentPage * itemsPerPage, (currentPage + 1) * itemsPerPage)
    : [];

  return (
    <div className="App">
      <h1>Investment Research</h1>
      <h3>A very simple react app to showcase AI Agent capabilities</h3>
      {error && <p className="error">{error}</p>}
      <div className="company-dropdown">
        <select
          value={selectedCompany}
          onChange={(e) => setSelectedCompany(e.target.value)}
        >
          <option value="" disabled>Select a company</option>
          {companies.map((company) => (
            <option key={company} value={company}>
              {company}
            </option>
          ))}
        </select>
      </div>
      <button onClick={handleResearch}>Research</button>
      {responseData && (
        <div className="response-data">
          <h2>Research Results</h2>
          <div className="paginated-content">
            {displayItems.map((item, index) => (
              <p key={index}>{item}</p>
            ))}
          </div>
          {/* <ReactPaginate
            previousLabel={'previous'}
            nextLabel={'next'}
            breakLabel={'...'}
            breakClassName={'break-me'}
            pageCount={pageCount}
            marginPagesDisplayed={2}
            pageRangeDisplayed={5}
            onPageChange={handlePageClick}
            containerClassName={'pagination'}
            subContainerClassName={'pages pagination'}
            activeClassName={'active'}
          /> */}
        </div>
      )}
    </div>
  );
}

export default App;
