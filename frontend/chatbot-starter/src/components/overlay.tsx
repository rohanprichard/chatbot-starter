import { motion, AnimatePresence } from "framer-motion"

interface OverlayProps {
  isOpen: boolean
  onClose: () => void
}

export function Overlay({ isOpen, onClose }: OverlayProps) {
  return (
    <AnimatePresence>
      {isOpen && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.3 }}
          className="fixed inset-0 bg-black bg-opacity-50 z-40 md:hidden"
          onClick={onClose}
        />
      )}
    </AnimatePresence>
  )
}

