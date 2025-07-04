import PropTypes from 'prop-types'

function Item({marca, ano_lancamento}) {
  return (
    <div>
      <li>
        {marca} - {ano_lancamento}
      </li>
    </div>
  );
}

Item.propTypes = {
  marca: PropTypes.string.isRequired,
  ano_lancamento: PropTypes.number,
};

Item.defaultProps = {
  marca: 'Faltou a marca',
  ano_lancamento: 0,
};

export default Item;