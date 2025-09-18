import style from "./LinkButton.module.css";
import { Link } from "react-router-dom";

function LinkButton({ to, text }) {
  return (
    <Link className={style.btn} to={to}>
      {text}
    </Link>
  );
}

export default LinkButton;
