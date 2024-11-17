import axios from 'axios';

export const GetTaros = async () => {
  try {
    const response = await axios.get(`http://go.itatmisis.ru:8000/get_taros/?status=three`);
    return response.data;
  } catch (e) {
    console.error(e);
  }
};
