import axios from 'axios';

export const postCompetency = async (id) => {
  try {
    const response = await axios.post(`http://go.itatmisis.ru:8000/post_competency_map/?id=${id}`);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
