import axios from 'axios';

export const postTaroSpread = async (taro_status, id) => {
  try {
    const response = await axios.post(
      `http://go.itatmisis.ru:8000/post_taro_spread/?taro_status=${taro_status}}&id=${id}`,
    );
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const postAnswer = async (question) => {
  try {
    const response = await axios.post(`http://go.itatmisis.ru:8000/post_answer/`, question);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
