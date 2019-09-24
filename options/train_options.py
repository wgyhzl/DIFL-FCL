from .base_options import BaseOptions


class TrainOptions(BaseOptions):
    def initialize(self):
        BaseOptions.initialize(self)
        self.isTrain = True

        self.parser.add_argument('--continue_train', action='store_true',
                                 help='continue training: load the latest model')
        self.parser.add_argument('--which_epoch', type=int, default=0,
                                 help='which epoch to load if continuing training')
        self.parser.add_argument('--phase', type=str, default='train',
                                 help='train, test (determines name of folder to load from)')

        self.parser.add_argument('--niter', required=True, type=int,
                                 help='# of epochs at starting learning rate (try 50*n_domains)')
        self.parser.add_argument('--niter_decay', required=True, type=int,
                                 help='# of epochs to linearly decay learning rate to zero (try 50*n_domains)')

        self.parser.add_argument('--lr', type=float, default=0.0002, help='initial learning rate for ADAM')
        self.parser.add_argument('--beta1', type=float, default=0.5, help='momentum term of ADAM')

        self.parser.add_argument('--lambda_cycle', type=float, default=10.0, help='weight for cycle loss (A -> B -> A)')
        self.parser.add_argument('--lambda_FCL', type=float, default=0.1,
                                 help='weight for latent-space-feature consistency loss')

        self.parser.add_argument('--save_epoch_freq', type=int, default=10,
                                 help='frequency of saving checkpoints at the end of epochs')
        self.parser.add_argument('--display_freq', type=int, default=100,
                                 help='frequency of showing training results on screen')
        self.parser.add_argument('--print_freq', type=int, default=100,
                                 help='frequency of showing training results on console')

        self.parser.add_argument('--no_lsgan', action='store_true',
                                 help='use vanilla discriminator in place of least-squares one')
        self.parser.add_argument('--pool_size', type=int, default=50,
                                 help='the size of image buffer that stores previously generated images')
        self.parser.add_argument('--train_using_cos', action='store_true',
                                 help='use cosine distance as loss metric while training')
        self.parser.add_argument('--domains_overlap', action='store_true',
                                 help='if specified, allow two identical domains for translation during training')