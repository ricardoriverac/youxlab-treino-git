import { FaFacebook, FaInstagram, FaLinkedin } from "react-icons/fa";
import styles from "./Footer.module.css";

function Footer() {
  return (
    <footer className={styles.footer}>
      <ul className={styles.fas}>
        <li>
          <FaFacebook className={styles.si}></FaFacebook>
        </li>
        <li>
            <FaInstagram className={styles.si}></FaInstagram>
        </li>
        <li>
            <FaLinkedin className={styles.si}></FaLinkedin>
        </li>
      </ul>
      <p className={styles.copyRigth}><span>Costs</span> &copy; 2025</p>
    </footer>
  );
}

export default Footer;
