import '../node_modules/react-vis/dist/style.css';
import {XYPlot, LineSeries, ArcSeries, RadialChart} from 'react-vis';

import { useState, useEffect } from 'react';

function Viz() {
  const [data, setData] = useState([]);
const myData = [{angle: 1}, {angle: 5}, {angle: 2}]
useEffect(() => {

  async function fetchMyAPI() {
    let response = await fetch("http://localhost:8000/app/get_data");


    response = await response.json();
    let tempData = response.data.total_rainfall
setData(response.data.total_rainfall)
  //  console.log(Object.keys(tempData).map(d => ({d}:tempData[d]})))
      setData(Object.keys(tempData).map((d,i) => ({angle:tempData[d],label:i+1})))

/*

    let group_students = await response.reduce((group, response) => {
      const {student_id} = response;
      group[student_id] = group[student_id] ?? [];
      group[student_id].push(response);
      return group;
    }, {});
*/


  }

console.log("start")
try {
  fetchMyAPI();
} catch (e) {
  console.log("error");

}



},[]);
  return (
    <div>
{data?

<RadialChart
  data={data}
  width={300}
  height={300}
    showLabels={true}/>
  :<h1>No data</h1>}



</div>
  )
}

export default Viz;
