import { useState, useEffect } from "react"
import axios from 'axios'

interface JobType {
  id: number;
  title: string;
  company: string;
  salary: number;
  description: string;
  url: string;
  location: string;

}

const App = () => {
  const [jobs, setJobs] = useState<Array<JobType>>([])
  const [error, setError] = useState<string>("")

  const fetchJobs = async() => {
    try{
      const response = await axios.get('http://127.0.0.1:8000/jobs')
      const jobData = response.data;
      console.log("job data: ",jobData)
      setJobs(jobData)
    } catch (err){
      setError('error getting job data')
      console.log('error fetching job data', err)
    }
    
    
  }
  useEffect(() => {
    fetchJobs()
  }, [])


  return (
    <div>
      {error && (<p className="text-red-500">{error}</p>)}
      <h1>Job listing</h1>
      {jobs.map((job) => (
        <div key={job.id}>
          <h2>{job.title}</h2>
          <p>{job.company} - {job.location}</p>
          <p>Salary: ${job.salary}</p>
          <p>{job.description}</p>
          <a href={job.url}>View Job</a>
        </div>
      ))}
    </div>
  ) 
}

export default App
