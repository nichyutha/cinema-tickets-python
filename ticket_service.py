from purchase_exceptions import InvalidPurchaseException
from paymentgateway.ticket_payment_service import TicketPaymentService
from seatbooking.seat_reservation_service import SeatReservationService


class TicketService:

    def __validate_account_id(account_id):
      '''
      This method validates account_Id
      '''
      if  (not isinstance(account_id,int)) or (account_id <= 0):
          raise InvalidPurchaseException('Invalid Account ID.')


    def __validate_and_count_tickets(ticket_type_requests):
      '''
      This method validates tickets and returns the count of tickets
      '''
      total_number_of_tickets = 0
      if len(ticket_type_requests) == 0:
        raise InvalidPurchaseException('Purchase atleast One Adult Ticket to Reserve Seat(s).')

      if 'ADULT' not in [ticket_request.ticket_type for ticket_request in ticket_type_requests]:
        raise InvalidPurchaseException('Child/Infant tickets cannot be purchased without purchasing an Adult ticket.')

      # Can number of INFANT tickest >  ADULT tickets ? If yes, It needs to be checked
      for ticket_request in ticket_type_requests:
        if 'INFANT' not in ticket_request.ticket_type:
          total_number_of_tickets += ticket_request.number_of_tickets
    
      if total_number_of_tickets > 20:
        raise InvalidPurchaseException('More than 20 tickets can\'t be purchased at a time.')
      else:
        return total_number_of_tickets

    
    def __calculate_ticket_price(ticket_type_requests):
      '''
      This method returns Total amount for purchasing tickets 
      '''
      total_ticket_purchase_price = 0
      for ticket_request in ticket_type_requests:
        if ticket_request.ticket_type == 'ADULT':
          total_ticket_purchase_price += 20 * ticket_request.number_of_tickets
        elif ticket_request.ticket_type == 'CHILD':
          total_ticket_purchase_price += 10 * ticket_request.number_of_tickets
        elif ticket_request.ticket_type == 'INFANT':
          total_ticket_purchase_price += 0 * ticket_request.number_of_tickets
      return total_ticket_purchase_price


    def __pay_and_reserve_seats(account_id,total_price,total_tickets):
      '''
      This method makes call to Payment service and Reservation service
      '''     
      paymentgateway = TicketPaymentService().make_payment(account_id,total_price)
      seatreservation = SeatReservationService().reserve_seat(account_id,total_tickets)

    """

      purchase_tickets should be the only public method

    """
    @staticmethod
    def purchase_tickets(account_id=None, ticket_type_requests=[]):
      
      try:
        TicketService.__validate_account_id(account_id)
        total_tickets = TicketService.__validate_and_count_tickets(ticket_type_requests)
        total_price = TicketService.__calculate_ticket_price(ticket_type_requests)
        TicketService.__pay_and_reserve_seats(account_id,total_price,total_tickets)
      except InvalidPurchaseException as ex: 
        print(ex)
      else:
        print (f'Payment £{total_price} was successful, {total_tickets} Seats were reserved !!')


